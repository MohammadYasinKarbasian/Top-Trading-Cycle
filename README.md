
# Top Trading Cycle Algorithm Implementation

This repository contains a Python implementation of the Top Trading Cycle Algorithm, a mechanism for solving the problem of allocating indivisible items or resources among agents with preferences. The algorithm is widely used in the field of matching theory, particularly in the context of school choice and house allocation problems.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Algorithm Description](#algorithm-description)
- [Test Files](#test-files)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Top Trading Cycle Algorithm is a mechanism designed to find a stable allocation of resources in a way that there are no incentives for agents to trade and improve their own allocation. It is a widely used algorithm in various allocation problems, including school assignments, house allocation problems, and more.

## Usage

To use this Python implementation of the Top Trading Cycle Algorithm, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/top-trading-cycle.git


2. Run the algorithm by executing the main Python script:

   ```bash
   python top_trading_cycle.py
   
3. Follow the prompts to provide the input data or specify the test file you want to use for allocation.

4. The algorithm will perform the allocation and display the results.

## Algorithm Description
The Top Trading Cycle Algorithm works as follows:

1. Agents express their preferences for items or resources.

2. Starting with an empty allocation, agents are matched in cycles of trades that improve their allocation.

3. A cycle is formed by tracing a path of trades where each agent agrees to trade with the next agent in the cycle.

4. Once a cycle is formed, the resources are reallocated according to the cycle, and the process continues until no more cycles can be formed.

5. The algorithm terminates when a stable allocation is reached, where no agent has an incentive to trade and improve their allocation.

## Test Files
This repository includes four test.txt files, which contain sample input data for testing the Top Trading Cycle Algorithm. You can use these files to validate the correctness and performance of the implementation. Each test file contains the preferences of agents.

* Test1.txt
* Test2.txt
* Test3.txt
* Test4.txt
## Contributing
Contributions to this project are welcome! If you have suggestions for improvements or bug fixes, please open an issue or create a pull request. For major changes, please discuss them in an issue first.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
