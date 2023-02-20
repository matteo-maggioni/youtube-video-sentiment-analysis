# Sentiment analysis dei commenti di un video di YouTube

### Pre-requisiti

- Python >= 3.7

### Setup

Per utilizzare il progetto è necessario avere un account Google per creare il **progetto** e l'**API key** sulla Google Developers Console.

Il processo è il seguenti:
1. avere/creare un account Google per accedere alla [Google API Console](https://console.cloud.google.com/)
2. creare un progetto dal menù a tendina nella barra in alto
3. abilitare il servizio **YouTube Data API v3** tramite il menù laterale > **API e Servizi** > **Libreria**
4. una volta abilitato, sempre dal menù laterale, accedere a **Credenziali** e creare la chiave API 

Andranno create le seguenti variabili d'ambiente (o sostutito il valore delle variabili):
- **API KEY**: in cui si va ad inserire quella appena creata
- **VIDEO ID**: l'id del video che è presente nel url youtube.com/watch?v=**L0HdC3qUAAA**

Maggiori informazioni per la creazione del progetto su Google Console son descritte qui: https://developers.google.com/youtube/v3/getting-started#before-you-start

