from .bow import Settings

pyramid = Settings(
    n_draw_steps = 150,
    n_limb_elements = 20,
    n_string_elements = 25,
    sampling_rate = 10000.0,
    time_span_factor = 1.5,
    time_step_factor = 0.2
)

recurve = Settings(
    n_draw_steps = 150,
    n_limb_elements = 20,
    n_string_elements = 30,
    sampling_rate = 10000.0,
    time_span_factor = 1.5,
    time_step_factor = 0.2
)
