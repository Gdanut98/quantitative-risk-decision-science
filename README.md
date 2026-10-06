# Quantitative Risk & Decision Science

A portfolio of decision-making methods for situations where uncertainty materially changes the recommended action.

## Methods
- Expected Monetary Value
- Decision Trees
- Sensitivity Analysis
- Value of Information
- Bayesian Updating
- Posterior Probabilities
- Risk Aversion
- Exponential Utility / Certainty Equivalent
- Monte Carlo Simulation
- Random-Variable Generation
- Correlated Inputs
- Central Limit Theorem experiments

## Tools
Python • Jupyter • NumPy/Pandas • Excel • decision-tree modeling

## Source-derived examples
### Arcade sensitivity
Game 3 initially had the highest EMV (0.20). Increasing Game 1 payoff caused it to become optimal once payoff exceeded approximately 30.5.

### StellarPath value of information
Expected payoff without new technology: ~$6M.
Expected payoff with new technology: ~$8.75M.
Maximum willingness to pay / VOI: ~$2.75M.

### Risk aversion
A risk-averse decision-tree exercise produced CE ≈$220.5K without information and ≈$222,741 with information before a $100K agency cost—only about $2.2K of risk-averse information value, so the agency was not justified.

### Bayesian information
A separate decision problem used unconditional signal probabilities and Bayes posterior probabilities. Expected value with information was 0.4615 versus 0.380 without information, for VOI ≈$81,500—below a $100K agency cost.

## Simulation
Course implementations included 10,000–100,000 repetitions and discrete, exponential, triangular and normal inputs, plus correlated uncertainty and sampling-distribution/CLT experiments.
