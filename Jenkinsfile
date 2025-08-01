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
                bat 'python main.py'
            }
        }

        stage('Test') {
            steps {
                echo "Testing code (if you have test cases)"
            }
        }
    }
}
