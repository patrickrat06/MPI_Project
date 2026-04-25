
import csv
#import time
from generator import INT_GENERATORS, FLOAT_GENERATORS, STRING_GENERATORS, SEED
from sorting import ALGORITHMS, FASTER_ALGORITHMS, NO_QUICKSORT, FASTER_ALG_NO_QUICKSORT, ONLY_QUICKSORT, benchmark

#experiment configuration

TIMEOUT_SECONDS = 300

SMALL_CONFIG = {"sizes":  [20, 30, 50, 100],
                "runs":   100000}

MEDIUM_CONFIG = {"sizes":  [1000, 5000, 10000, 50000],
                "runs":   10}

LARGE_CONFIG = {"sizes":   [100_000, 500_000, 1_000_000],
                "runs":    3,
                "algorithms": FASTER_ALGORITHMS}

SMALL_GENERATORS  = FLOAT_GENERATORS
MEDIUM_GENERATORS = FLOAT_GENERATORS
LARGE_GENERATORS  = FLOAT_GENERATORS

OUTPUT_FILE = "results/results.csv"

#runner

def run_experiment(config, generators, algorithms=None):

    if algorithms is None:
        algorithms = ALGORITHMS

    rows = []
    sizes    = config["sizes"]
    n_runs   = config["runs"]

    for size in sizes:
        for struct_name, gen_fn in generators.items():
            data = gen_fn(size)

            for alg_name, alg_fn in algorithms.items():
                avg_time = benchmark(alg_fn, data, n_runs=n_runs, timeout=TIMEOUT_SECONDS)
                # benchmark() returns None if the timeout was hit,
                # or a float (seconds) if it completed in time.

                timed_out = (avg_time is None)

                row = {
                    "algorithm": alg_name,
                    "structure": struct_name,
                    "size": size,
                    "runs": n_runs,
                    "avg_time_s": round(avg_time, 9) if not timed_out else "TIMEOUT",
                    "avg_time_ms": round(avg_time * 1000, 6) if not timed_out else "TIMEOUT",
                    "timed_out": timed_out,
                    "seed": SEED,}
                rows.append(row)

                #printing results as they come in
                if timed_out:
                    print(f" {'TIMEOUT':15} | {alg_name:15} | {struct_name:20} | "
                          f"size={size:>8,} (>{TIMEOUT_SECONDS}s)")
                else:
                    print(f" {alg_name:15} | {struct_name:20} | size={size:>8,} | "
                          f"{avg_time * 1000:10.4f} ms | {n_runs} runs")

    return rows

def save_results(rows, filename):
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nResults saved to {filename}  (seed: {SEED})")

#main

if __name__ == "__main__":
    all_rows = []

    print("~" * 11)
    print("SMALL SIZES (seed: {SEED})")
    all_rows += run_experiment(SMALL_CONFIG, SMALL_GENERATORS)

    print("\n" + "~" * 12)
    print("MEDIUM SIZES")
    all_rows += run_experiment(MEDIUM_CONFIG, MEDIUM_GENERATORS)

    print("\n" + "~" * 11)
    print("LARGE SIZES")
    all_rows += run_experiment(LARGE_CONFIG, LARGE_GENERATORS, algorithms=LARGE_CONFIG["algorithms"])

    save_results(all_rows, OUTPUT_FILE)
    print("\nDone!")