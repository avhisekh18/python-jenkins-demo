pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning GitHub repo..."
            }
        }

        stage('Build') {
            steps {
                echo "Building the project (e.g., compiling code)"
            }
        }

        stage('Run Python App') {
            steps {
                echo "Running the Python app..."
                bat 'C:\\Users\\avhis\\AppData\\Local\\Programs\\Python\\Python313\\python.exe calc\\calculator.py'


            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests using pytest...'
                bat 'C:/Users/avhis/AppData/Local/Programs/Python/Python313/python.exe -m pytest'
            }
        }
    }
}
