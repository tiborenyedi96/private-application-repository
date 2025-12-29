pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKERHUB_USER = 'tenyedi96'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    stages {
        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t ${DOCKERHUB_USER}/incident-logger-frontend:${IMAGE_TAG} -f dockerfile .'
                }
            }
        }
        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'docker build -t ${DOCKERHUB_USER}/incident-logger-backend:${IMAGE_TAG} -f dockerfile .'
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                sh '''
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push ${DOCKERHUB_USER}/incident-logger-frontend:${IMAGE_TAG}
                    docker push ${DOCKERHUB_USER}/incident-logger-backend:${IMAGE_TAG}
                '''
            }
        }
        stage('Copy Helm Chart') {
            steps {
                sh '''
                    scp -i /var/lib/jenkins/.ssh/id_rsa -P 2233 -r incident-logger-chart udemx@192.168.1.185:/tmp/
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    ssh -i /var/lib/jenkins/.ssh/id_rsa -p 2233 udemx@192.168.1.185 \
                    "helm upgrade --install incident-logger /tmp/incident-logger-chart \
                     --set frontend.image.repository=${DOCKERHUB_USER}/incident-logger-frontend \
                     --set frontend.image.tag=${IMAGE_TAG} \
                     --set backend.image.repository=${DOCKERHUB_USER}/incident-logger-backend \
                     --set backend.image.tag=${IMAGE_TAG} \
                     --set imagePullSecrets[0].name=dockerhub-secret \
                     -n udemx"
                '''
            }
        }
    }
    post {
        success {
            echo "Deployment successful! Build: ${IMAGE_TAG}"
        }
        always {
            sh 'docker logout'
        }
    }
}


