# Docker

clone project:\
`git clone git@github.com:huydnt1801/democicd.git`\
mở code bằng VS Code:\
`code democicd`\
build docker image:\
`docker build -t tên:v1 .`\
xem các image:\
`docker images`\
chạy image:\
`docker run -p port_local:port_container id/tên_image`\
xem các container đang chạy:\
`docker ps`\
push image lên docker hub. lưu ý: để đẩy được image lên hub, bạn cần đặt tên image theo chuẩn sau: tên_tk_hub_của_bạn/tên_image:tag\
bạn cần đăng nhập trước: `docker login`\
đẩy lên hub: `docker push tên_image:tag`\
tham khảo: https://viblo.asia/p/su-dung-docker-push-de-publish-mot-image-len-docker-hub-L4x5xgYblBM

# Kubernetes

install K8S:\
`https://kubernetes.io/vi/docs/tasks/tools/install-kubectl/`\
install Minikube:\
`https://kubernetes.io/vi/docs/tasks/tools/install-minikube`\
chaỵ minikube:\
`minikube start`\
chuyển context:\
`kubectl config use-context tên_context`\
khi bạn dùng minikube làm cluster thì tên*context là `minikube`\  
kiểm tra pods ở namespace default:\
`kubectl get pods`\
thêm -n tên_namespace để lấy thông tin ở namespace khác\
xem thay đổi liên tục của pod trên namespace default:\
`watch kubectl get pods -n default`\
apply config mới:\
`kubectl apply -f địa_chỉ*đến_file_manifest`\
xóa 1 pod:\
`kubectl delete -n default pod tên_pod`\
xóa hết ở namespace default:\
`kubectl delete all --all -n default`\
thêm ingress:\
`minikube addons enable ingress`\
forward port 3000 of localhost to port 80 of service ingress:\
`kubectl -n ingress-nginx port-forward service/ingress-nginx-controller 3000:80`
