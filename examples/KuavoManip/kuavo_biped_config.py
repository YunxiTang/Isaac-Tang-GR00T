from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import (
    ActionConfig,
    ActionFormat,
    ActionRepresentation,
    ActionType,
    ModalityConfig,
)


kuavo_biped_config = {
    'state': ModalityConfig(
        delta_indices=[0,],
        modality_keys=['left_arm', 'right_arm', 'gripper'],
    ),
    'video': ModalityConfig(
        delta_indices=[0,],
        modality_keys=['head', 'left', 'right'],
    ),
    'action': ModalityConfig(
        delta_indices=list(range(0, 16)),
        modality_keys=['left_arm', 'right_arm', 'gripper'],
        action_configs=[
            # left arm
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT
            ),
            # right arm
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT
            ),
            # gripper
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,
                format=ActionFormat.DEFAULT
            ),
        ]
    ),
    'language': ModalityConfig(
        delta_indices=[0,],
        modality_keys=['annotation.human.task_description',],
    ),
}

register_modality_config(kuavo_biped_config)