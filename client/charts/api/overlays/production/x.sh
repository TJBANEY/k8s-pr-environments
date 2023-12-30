# Change directory to Kustomize overlays based on environment
cd "chart/overlays/$ENVIRONMENT" || exit

# Use kustomize on overlay to produce new k8s manifests
kustomize edit set image "$ACCOUNT.dkr.ecr.$REGION.amazonaws.com/$APP:$VERSION"

# Apply manifests to cluster to update resources
kubectl apply -k .

-k, --kustomize='':
Process a kustomization directory. Cant be used together with -f or -R


apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
- ../../base

patchesStrategicMerge:
- hpa.yaml


--------------------------------------------

- Base

- Overlays       ====> 'Static patches' like patching a soldiers uniform
---- Dev 
---- Staging
---- Production


kustomize edit set image "$ACCOUNT.dkr.ecr.$REGION.amazonaws.com/$APP:$VERSION"

Edits a property on the static patch 'kustomization.yaml'. Gives you the ability to
make things 'Dynamic'!!

AGAIN

kustomize edit = Make changes to patches 'on the fly' aka 'make dynamic'