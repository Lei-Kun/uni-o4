from copy import deepcopy
from transition_model.configs.neorl.default import default_args


hopper_v3_low_args = deepcopy(default_args)
hopper_v3_low_args["rollout_length"] = 5
hopper_v3_low_args["penalty_coef"] = 2.5
hopper_v3_low_args["auto-alpha"] = False