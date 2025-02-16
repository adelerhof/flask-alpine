node {
    stage('Checkout SCM') {
        checkout scm
        sh "git rev-parse --short HEAD > commit-id"
        tag = readFile('commit-id').replace("\n", "").replace("\r", "")
        appname = "flask-alpine:"
        registryHost = "registry.adelerhof.eu:49086/"
        env.imageName = "${registryHost}${appname}${tag}"
        env.BUILD_TAG=tag
    }

    stage ('Build') {
        sh "docker build -t flask-alpine:1 ."
    }
        
    // docker.image('flask-alpine:1').inside {
    //     stage('Test') {
    //         sh 'coverage run test_app.py'
    //         sh 'coverage xml -o coverage-reports/coverage-.xml'
    //         sh 'pytest --junitxml=reports/results.xml'
    //         junit 'reports/*.xml'
    //         cobertura coberturaReportFile: 'coverage-reports/coverage-.xml'
    //     }
    // }
    
    stage('SonarQube') {
        def scannerHome = tool 'scanner';
        withSonarQubeEnv('SonarQube') {
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=flask-alpine -Dsonar.sources=."
        }
    }

    stage('Rename image') {
        sh "docker tag flask-alpine:1 ${imageName}"
        sh "docker tag flask-alpine:1 flask-alpine:latest"
    }
    
    stage ('Push') {
        docker.withRegistry('https://registry.adelerhof.eu:49086', 'registry.adelerhof.eu') {
            def customImage = docker.build("${imageName}")
            customImage.push()
            // sh "docker push ${imageName}"
        }
    }

    stage ('Push Latest') {
        docker.withRegistry('https://registry.adelerhof.eu:49086', 'registry.adelerhof.eu') {
            def customImage = docker.build("flask-alpine:latest")
            customImage.push()
            // sh "docker push ${imageName}"
        }
    }

    // stage ('Deploy') {
    //     sh "sed 's#127.0.0.1:30400/flask-alpine:version#127.0.0.1:30400/flask-alpine:'$BUILD_TAG'#' deployment.yaml | kubectl apply -f -"
    // }
    
    stage ('Clean') {
        sh "docker rmi -f flask-alpine:1"
        sh "docker rmi -f ${imageName}"
        sh "docker rmi -f flask-alpine:latest"
    }
}
        
