from globus_compute_sdk import Executor as GCExecutor

# Replace local agent execution with remote executor
executor = GCExecutor(
    endpoint="<MIDWAY_ENDPOINT_ID>",  # Use the UUID from Step 5
    exchange_url="https://exchange.academy-agents.org"
)

# Example: submit a function to run a tournament
def run_remote_tournament():
    # import and run your TournamentAgent logic here
    import simple_tournament
    # Start tournament logic, maybe register some players, etc.

# Submit to remote Midway endpoint
future = executor.submit(run_remote_tournament)
print(f"Submitted job: {future.result()}")
