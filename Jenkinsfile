pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Files Exist') {
            steps {
                script {
                    def htmlExists = fileExists 'index.html'
                    if (!htmlExists) {
                        error("index.html file not found in the repository!")
                    } else {
                        echo "index.html exists."
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\abhyu\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" test_form.py'
            }
        }
    }
    
    post {
        success {
            echo "All tests passed! The HTML form is valid and ready."
        }
        failure {
            echo "Tests failed. Please check the test script output."
        }
    }
}
