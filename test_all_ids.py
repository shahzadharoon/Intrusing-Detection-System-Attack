from tabulate import tabulate
from test_ids import test
from train_ids import parse_arguments
from yaml import load, Loader

IDS_CONFIGS = [
    ('baseline', 'configs/baseline.yaml'),
    ('decision_tree', 'configs/decision_tree.yaml'),
    ('k_nearest_neighbors', 'configs/k_nearest_neighbors.yaml'),
    ('logistic_regression', 'configs/logistic_regression.yaml'),
    ('multi_layer_perceptron', 'configs/multi_layer_perceptron.yaml'),
    ('naive_bayes', 'configs/naive_bayes.yaml'),
    ('random_forest', 'configs/random_forest.yaml'),
    ('support_vector_machine', 'configs/support_vector_machine.yaml')
]

def main():
    results = list(map(test_configuration, IDS_CONFIGS))
    print_results(results)

def test_configuration(configuration):
    name, config_path = configuration
    options = parse_arguments(['--config', config_path])
    scores = test(options)
    named_scores = [name, *scores]
    return named_scores

def print_results(results):
    rows = list(map(format_result, results))
    headers = ['algorithm', 'accuracy', 'f1', 'precision', 'recall']
    print(tabulate(rows, headers=headers))

def format_result(result):
    scores = map(lambda score: f'{score:0.4f}', result[1:])
    formatted_result = [result[0], *scores]
    return formatted_result

if __name__ == '__main__':
    main()