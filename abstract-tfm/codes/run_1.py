import time
import logging
from engine import Engine
from config import Config
from run_config import RunConfig
from stats import Stats

REPEATS = 200

def simulation():
    results = []

    config = Config()
    run_config = RunConfig(config)

    run_config.section_length = 500
    run_config.road_length = 5000
    run_config.n_lanes = 2
    run_config.time_steps = 1000
    run_config.driver_type_density = [1.0, 0.0, 0.0, 0.0, 0.0]
    run_config.verbose = False
    run_config.accident_max_threshold = 0.10

    population_sizes = [a for a in range(10, 110, 10)]

    for i in range(0, 10):
        run_config.population_size = population_sizes[i]

        for j in range(0, REPEATS):
            engine = Engine(run_config)
            engine.run()

            # Check if the simulation was valid (accidents < 10%)
            if not engine.validate_simulation():
                # ... manage the error

            stats = Stats(engine=engine)
            results.append(stats)

    # ... print time
    # ... save results to file
