const firebaseConfig = {
    apiKey: process.env.CLOUD_APIKEY,
    authDomain: process.env.CLOUD_AUTH_DOMAIN,
    databaseURL: process.env.CLOUD_DATABASE_URL,
    projectId: process.env.CLOUD_PROJECT_ID,
    storageBucket: process.env.CLOUD_STORAGE_BUCKET,
    messagingSenderId: process.env.CLOUD_MESSAGING_SENDER_ID,
    appId: process.env.CLOUD_APP_ID,
    measurementId: process.env.CLOUD_MESSUREMENT_ID
  };

  export default firebaseConfig;
