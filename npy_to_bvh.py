from argparse import ArgumentParser

import numpy as np

from Motion import BVH
from Motion.InverseKinematics import animation_from_positions


def smpl2bvh(motion_path: str, bvh_path: str) -> None:
    pos = np.load(motion_path, allow_pickle=True).item()["motion"]
    pos = pos.transpose(0, 3, 1, 2)  # samples x joints x coord x frames ==> samples x frames x joints x coord
    parents = [-1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 12, 13, 14, 16, 17, 18, 19]
    SMPL_JOINT_NAMES = [
        "Pelvis", "L_Hip", "R_Hip", "Spine1", "L_Knee", "R_Knee", "Spine2", "L_Ankle", "R_Ankle",
        "Spine3", "L_Foot", "R_Foot", "Neck", "L_Collar", "R_Collar", "Head", "L_Shoulder",
        "R_Shoulder", "L_Elbow", "R_Elbow", "L_Wrist", "R_Wrist", "L_Hand", "R_Hand",
    ]
    for i, p in enumerate(pos):
        print(f"starting anim no. {i}")
        anim, sorted_order, _ = animation_from_positions(p, parents)
        BVH.save(bvh_path.format(i), anim, names=np.array(SMPL_JOINT_NAMES)[sorted_order])

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--prompt", type=str, required=True)
    args = parser.parse_args()

    motion_path = "motion-diffusion-model/results/results.npy"
    bvh_path = "AnimatedDrawings/examples/bvh/my_motion.bvh"
    smpl2bvh(motion_path, bvh_path)
