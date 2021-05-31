Hello, everyone. I am glad to share my recent research with you here. In this brief presentation, I will talk about the novel regularization technique presented in this paper, named adversarial model perturbation.

Effective regularization schemes alleviate overfitting and improve generalization. Look at the two figures, the left figure sketches the model's behavior without regularization, which can only achieve a large generalization error on a relatively small capacity.  However, in the right figure, the model can achieve a small generalization error on a relatively large capacity. Some researchers have found the modern neural networks may have different behavior, that is, the Double Descent. Nevertheless, well-regularized neural networks consistently achieve better performance in practice.

Previous work suggested that the flat minima can improve generalization both in theoretical and empirical perspectives. So in this work, we propose a powerful regularization scheme principled by the objective of finding flat minima.

In Adversarial Model Perturbation, we minimize an alternative AMP loss. The AMP loss is derived from the empirical risk by applying the worst perturbation on the model parameters. As sketched in the figures, it applies a max-pooling operation on the empirical risk to seek a flatter minimum.

In the AMP training procedure, we adopt a mini-batch SGD for solving the min-max problem. We firstly update delta to maximize ERM loss via gradient ascent, and then update theta to minimize ERM loss via gradient descent.

We implemented AMP with PyTorch. The AMP is very easy to use, you can just replace the optimization steps with the following lines to regularize your own neural network models.

Now we will give some theoretical justifications about AMP. We assume that the loss surface of each local minimum in ERM loss can be locally approximated as an inverted Gaussian surface \gamma with a mean vector \mu and a covariance matrix \kappa.

Under the locally Gaussian assumption, the empirical risk is minimized when \theta equals \mu and the minimum value is C minus A. The minimum value of the AMP loss is the empirical risk at the location in the narrowest principal direction of the cross-section of the loss surface, where \sigma square is the smallest eigenvalue of \kappa. It is clear that \gamma_AMP star although related to the minimum value of empirical risk, it also takes into account the curvature of the surface around the local minimum. Thus we can find a flatter minimum by minimizing the AMP loss.

On the other hand, AMP can regularize gradient norm. Consider that N equals one, which is in fact used in our experiments. The AMP training is equivalent to ERM training with an additional term. Thus, the AMP training algorithm effectively tries to find the local minima of empirical risk that not only have low values, but also have small gradient norms near the minima. Note that a minimum with smaller gradient norms around it is a flatter minimum.

Now we have given the formulation and justifications of AMP. We also conducted extensive experiments to validate the effectiveness of AMP. Here is the setup of our experiments.

Firstly, we find that AMP has a larger training loss but smaller test loss than ERM training.

On three image classification benchmarks, AMP achieves the best performance among the compared regularization schemes.

Furthermore, AMP can improve the model's performance over powerful data augmentation techniques.

Besides, AMP is capable of reducing the calibration error of neural networks.

We also investigated the relationship between loss values and the perturbation sizes. A proper perturbation size helps the model achieve the best test loss.

We visualized the landscape of the selected minima of ERM and AMP. We found that the minima found by AMP are flatter than ERM.

That is all. Thanks for listening.

