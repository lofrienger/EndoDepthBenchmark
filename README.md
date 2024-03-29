# EndoDepthBenchmark


## Introduction

Accurate depth perception is crucial for patient outcomes in endoscopic surgery, yet it is compromised by image distortions common in surgical settings. As shown in the image below, the depth estimation model's performance degrades significantly when the input image is corrupted.

![image](assets/images/depth_under_corrupt.png)

Our study introduces a benchmark for evaluating the robustness of endoscopic depth estimation models. We've compiled a dataset with synthetically induced corruptions at different intensities. We also present the Depth Estimation Robustness Score (*DERS*), a new metric combining error, accuracy, and robustness measures. This metric and benchmark aim to improve model refinement and reliability under adverse conditions. Our findings highlight the need for robust algorithms, contributing to surgical precision and patient safety.





![image](assets/images/ders.png)


## Corrupted Dataset

we utilize the [SCARED](https://endovissub2019-scared.grand-challenge.org/) as the base dataset. We have introduced a range of synthetic corruptions to the SCARED dataset to create a new dataset, which we refer to as the Corrupted SCARED (C-SCARED) dataset. The C-SCARED dataset contains 1,000 images, each with 5 levels of corruption. The corruptions are applied to the images in the dataset at varying intensities, with each level of corruption representing a different intensity. The levels of corruption are as follows:


### Dataset Structure



## Metrics

### Accuracy and Error Metrics


### Depth Estimation Robustness Score (DERS)

*DERS* purposefully devised to combine three pivotal components—error, accuracy, and robustness—into a comprehensive composite index.

     \ metrics
level   abs_rel, sq_rel, rmse, rmse_log, a1, a2, a3
0
1
2
3
4
5