pipeline {
    agent any
    environment {
        PYTHON_VERSION = '3.9'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        // stage('Setup Python') {
        //     steps {
        //         bat "python -m venv env"
        //         bat "source env/bin/activate"
        //         bat "pip install --upgrade pip"
        //         bat "pip install -r requirements.txt"
        //         bat "pip install pytest"
        //         bat "pip install pylint"
        //         bat "pip install black"
        //     }
        // }
        stage('Run Tests') {
            steps {
                bat "pytest unittesting/test_cases.py"
            }
            post {
                always {
                    junit 'pytest.xml'
                }
            }
        }
        stage('Code Linting') {
            steps {
                bat "pylint setup.py"
                bat "black unittesting/test_cases.py"
            }
        }
        // stage('Merge to master branch') {
        //     when {
        //         expression { currentBuild.result == 'SUCCESS' }
        //     }
        //     steps {
        //         bat "git checkout master"
        //         bat "git merge ${env.BUILD_NUMBER} --no-ff -m 'Merge saroobat branch'"
        //         bat "git push origin master"
        //     }
        // }
    }
}
