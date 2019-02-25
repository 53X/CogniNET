# CogniNET [[pdf](https://arxiv.org/pdf/1811.00201.pdf)]
The **CogniNet** is a recurrent model that can perform classification of EEG signals, as well as function as a feature extractor for further applications. 

**Please note that this is not the complete code for the work. The complete code  and the replication details will be published once this paper gets accepted in a peer-reviewed conference.**  

**The dataset that has been used in this work was originally released at CVPR 2017 by [Spampinato et.al](https://arxiv.org/abs/1609.00344) where the authors have claimed this dataset to be the largest EEG signal dataset for visual object analysis. It has also been used in a follow-up work by [Palazzo et.al](https://arxiv.org/abs/1609.00344) published at ICCV 2017. Also note that, this dataset requires the downloading of images from ImageNet against their corresponding EEG signals. Since the dataset has been publicly released in the above mentioned work, we are no way responsible for the distribution of the dataset and the corresponding images and hence will also not take part in the same. Thus for issues relating to dataset download/distribution and ethical issues relating to dataset curation, please contact the authors of the original work.**


## Abstract
Can we ask computers to recognize what we see from brain signals alone? Our paper seeks to utilize the knowledge learnt in the visual domain by popular pre-trained vision models and use it to teach a recurrent model being trained on brain signals to learn a discriminative manifold of the human brain's cognition of different visual object categories in response to perceived visual cues. For this we make use of brain EEG signals triggered from visual stimuli like images and leverage the natural synchronization between images and their corresponding brain signals to learn a novel representation of the cognitive feature space. The concept of knowledge distillation has been used here for training the deep cognition model, the CogniNet, by employing a student-teacher learning technique in order to bridge the process of inter-modal knowledge transfer. The proposed novel architecture obtains state-of-the-art results, significantly surpassing other existing models. The experiments performed by us also suggest that if visual stimuli information like brain EEG signals can be gathered on a large scale, then that would help to obtain a better understanding of the largely unexplored domain of human brain cognition.

## Model Architecture
<center><img src="https://github.com/codebuddha/CogniNET/blob/master/BrainNet.jpg" align="middle"></center>






