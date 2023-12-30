import argparse
import yaml
import os

def generate_manifest(pr_number, app_name, manifest_path):
    # Define a base structure of your Ingress manifest
    manifest = {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "Ingress",
        "metadata": {
            "name": "{}-ingress".format(app_name),
            "annotations": {
                "kubernetes.io/ingress.class": "nginx",
                # Add any other necessary annotations
            }
        },
        "spec": {
            "rules": [
                {
                    "host": "pr-{}-{}.yourdomain.com".format(pr_number, app_name),
                    "http": {
                        "paths": [
                            {
                                "path": "/",
                                "pathType": "Prefix",
                                "backend": {
                                    "service": {
                                        "name": "{}-service".format(app_name),
                                        "port": {
                                            "number": 80
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

    with open(os.path.join(manifest_path, 'ingress.yaml'), 'w') as outfile:
        yaml.dump(manifest, outfile)

def main():
    parser = argparse.ArgumentParser(description="Generate K8s Ingress manifests")
    parser.add_argument("pr_number", help="Pull request number")
    args = parser.parse_args()

    # Define your application names and their relative Kubernetes manifest directories
    apps = {
        "react": "client/charts/web/base",
        "django": "client/charts/api/base",
    }

    for app_name, manifest_path in apps.items():
        generate_manifest(args.pr_number, app_name, manifest_path)

if __name__ == "__main__":
    main()