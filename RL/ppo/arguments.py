import argparse
import torch

#windows (tested): 5 processes, 10 envs per, 15 mini batch, 4 eval processes
#same for local mac but not tested
#mostly did 600 steps but think this is too much. might drop to 300
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--lr', type=float, default=3e-4
    )
    parser.add_argument(
        '--use-linear-lr-decay', action='store_true', default=True
    )
    parser.add_argument(
        '--eps', type=float, default=1e-5, help="ADAM optimiser epsilon"
    )
    parser.add_argument(
        '--gamma', type=float, default=0.999, help="discount factor"
    )
    parser.add_argument(
        '--gae-lambda', type=float, default=0.95
    )
    parser.add_argument(
        '--entropy-coef-start', type=float, default=0.04
    )
    parser.add_argument(
        '--entropy-coef-final', type=float, default=0.005
    )
    parser.add_argument(
        '--entropy-coef-start-anneal', type=int, default=500
    )
    parser.add_argument(
        '--entropy-coef-end-anneal', type=int, default=1500
    )
    parser.add_argument(
        '--dense-reward-anneal-start', type=int, default=-1
    )
    parser.add_argument(
        '--dense-reward-anneal-end', type=int, default=-500
    )
    parser.add_argument(
        '--value-loss-coef', type=float, default=1.0
    )
    parser.add_argument(
        '--max-grad-norm', type=float, default=0.5
    )
    parser.add_argument(
        '--seed', type=int, default=0
    )
    parser.add_argument(
        '--num-processes', type=int, default=24
    )
    parser.add_argument(
        '--num-envs-per-process', type=int, default=5
    )
    #The number of decisions the agent being trained (i.e. the agent with the most recent policy) should make in each game on each process.
    #default 200 (for 4p)
    parser.add_argument(
        '--num-steps', type=int, default=200
    )
    parser.add_argument(
        '--truncated-seq-len', type=int, default=10
    )
    parser.add_argument(
        '--ppo-epoch', type=int, default=10
    )
    #The number of minibatches each epoch is broken up into (so each epoch consists of this many gradient updates to the model).
    #default 64
    #So each minibatch is made up of (128 * 5 * 200) = 128,000 / 64 = 2000 samples. 
    #Whilst I think this is reasonable, I have to say I'm not completely sure.

    #So we have 2000 samples (5 * 10 * 600) = 30,000 / 15 = 2,000
    #default was 200
    parser.add_argument(
        '--num-mini-batch', type=int, default=12
    )
    parser.add_argument(
        '--clip-param', type=float, default=0.2
    )
    parser.add_argument(
        '--total-env-steps', type=int, default=1e9
    )
    parser.add_argument(
        '--recompute-returns', action='store_true', default=True
    )
    parser.add_argument(
        '--no-cuda', action='store_true', default=False
    )
    parser.add_argument(
        '--cuda-deterministic', action='store_true', default=False
    )
    parser.add_argument(
        '--num-policies-to-store', type=int, default=500
    )
    parser.add_argument(
        '--add-policy-every', type=int, default=4, help='add new policy every this many updates'
    )
    parser.add_argument(
        '--update-opponent-policies-every', type=int, default=1
    )
    #default = 25
    parser.add_argument(
        '--eval-every', type=int, default=50
    )
    parser.add_argument(
        '--num-eval-episodes', type=int, default=128
    )
    parser.add_argument(
        '--num-eval-processes', type=int, default=12
    )
    parser.add_argument(
        '--load-from-checkpoint', action='store_true', default=False
    )
    parser.add_argument(
        '--load-file-path', type=str, default=""
    )
    parser.add_argument(
        '--expt-id', type=str, default="default"
    ),
    parser.add_argument(
        '--update_timeout', type=int, default=15
    )

    args = parser.parse_args()

    args.cuda = not args.no_cuda and torch.cuda.is_available()

    return args
