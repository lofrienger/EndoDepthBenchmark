
import numpy as np

clean_metrics = np.array([0.069, 0.584, 5.574, 0.094, 0.947, 0.998, 1.000])

# Accuracy weights:
W_ACC = np.array([0.5, 0.3, 0.2])

def calculate_derm(metrics_array, accuracy_weights=W_ACC, lambd=1.0):
    # Error component calculation
    error_norms = metrics_array[0, :4] # Error norms for normalization (error metrics on clean images)
    mean_errors = metrics_array[1:, :4].mean(axis=0)
    normalized_errors = mean_errors / error_norms
    
    # Accuracy component calculation
    mean_accuracies = metrics_array[:, 4:].mean(axis=0)
    weighted_accuracies = mean_accuracies * accuracy_weights
    accuracy_component = np.sum(weighted_accuracies)

    # Robustness component calculation
    deviations = metrics_array[1:, :] - metrics_array[0, :]
    robustness = np.mean(np.std(deviations, axis=0))
    
    # Final DERM calculation
    derm_score = np.sum(normalized_errors) / accuracy_component * np.exp(-lambd * robustness)
    # derm_score = lambd * robustness * np.sum(normalized_errors) / accuracy_component
    
    return derm_score


def compute_errors(gt, pred):
    """Computation of error metrics between predicted and ground truth depths
    """
    thresh = np.maximum((gt / pred), (pred / gt))
    a1 = (thresh < 1.25     ).mean()
    a2 = (thresh < 1.25 ** 2).mean()
    a3 = (thresh < 1.25 ** 3).mean()

    rmse = (gt - pred) ** 2
    rmse = np.sqrt(rmse.mean())

    rmse_log = (np.log(gt) - np.log(pred)) ** 2
    rmse_log = np.sqrt(rmse_log.mean())

    abs_rel = np.mean(np.abs(gt - pred) / gt)

    sq_rel = np.mean(((gt - pred) ** 2) / gt)

    return abs_rel, sq_rel, rmse, rmse_log, a1, a2, a3



if __name__ == "__main__":
    pass
