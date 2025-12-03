pipeline{
    agent any
    stages{
        stage('Build docker image'){
            bat "docker build -t appdeployment:v1 ."
        }
        stage('Docker login'){
            bat "docker login -u 22251a1257it258 -p Manogna18@gnits"
        }
        stage('Push docker image'){
            bat "docker rm -f mycontainer || exit 0"
            bat "docker tag appdeployment:v1 22251a1257it258/myapp:v1"
            bat "docker push 22251a1257it258/myapp:v1"
        }
        stage('Kubernetes deployment'){
            bat "kubectl apply -f deployment.yaml --validate=false"
            bat "kubectl apply -f service.yaml"
        }
        post{
            success{
                echo "success"
            }
            failure{
                echo "failed"
            }
        }
    }
}