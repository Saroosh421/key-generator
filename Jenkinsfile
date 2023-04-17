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
        stage('Setup Python') {
            steps {
                sh "python3 -m venv env"
                sh "source env/bin/activate"
                sh "pip install --upgrade pip"
                sh "pip install -r requirements.txt"
                sh "pip install pytest"
                sh "pip install pylint"
                sh "pip install black"
            }
        }
        stage('Run Tests') {
            steps {
                sh "pytest unittesting/test_cases.py"
            }
            post {
                always {
                    junit 'pytest.xml'
                }
            }
        }
        stage('Code Linting') {
            steps {
                sh "pylint unittesting/test_cases.py"
                sh "black unittesting/test_cases.py"
            }
        }
        // stage('Merge to master branch') {
        //     when {
        //         expression { currentBuild.result == 'SUCCESS' }
        //     }
        //     steps {
        //         sh "git checkout master"
        //         sh "git merge ${env.BUILD_NUMBER} --no-ff -m 'Merge saroosh branch'"
        //         sh "git push origin master"
        //     }
        // }
    }
}
