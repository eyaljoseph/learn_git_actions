{{/* Generate basic labels */}}
{{- define "dockerhub-app.labels" -}}
app-group: dockerhub-app
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/* Generate app specific labels */}}
{{- define "dockerhub-app.appLabels" -}}
app: {{ .name }}
{{- end -}}
