# CAP Round Predictor

CAP Round Predictor is a tool designed to predict the chances of admission to various colleges based on your performance in the CAP (Centralized Admission Process) rounds. It helps students make informed decisions about their preferences during the counseling process.

## Features

- Predict admission chances based on entered scores and rank.
- Analyze historical data to provide insights.
- User-friendly interface for easy input and output.
- Provides a list of potential colleges and branches.

## Prerequisites

To run this project, you will need:

- Python 3.8 or later
- Required libraries: 
  - pandas
  - numpy
  - scikit-learn
  - flask (if using a web interface)

Install the libraries using pip:

```bash
pip install pandas numpy scikit-learn flask
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SaeeS4/cap-round-predictor.git
```

2. Navigate to the project directory:

```bash
cd cap-round-predictor
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

3. Enter your CAP round details, including rank and preferences, to get predictions.

## Project Structure

```
cap-round-predictor/
|
|-- data/               # Contains historical admission data
|-- models/             # Machine learning models
|-- static/             # Static files (CSS, JS, images)
|-- templates/          # HTML templates for the web interface
|-- app.py              # Main application file
|-- requirements.txt    # Python dependencies
|-- README.md           # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature-name
```

3. Commit your changes:

```bash
git commit -m "Add feature-name"
```

4. Push to the branch:

```bash
git push origin feature-name
```

5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, feel free to contact:

- **Name:** Saee S.
- **GitHub:** [SaeeS4](https://github.com/SaeeS4)

---

Happy predicting! 🎉
