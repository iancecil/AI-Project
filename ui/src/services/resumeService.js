import axios from 'axios'

const baseURL = 'http://127.0.0.1:8080'

export const postResume =   async (cv_file, onProgress) =>{
    const formData = new FormData()
    // console.log('CV_FILE', cv_file)
    formData.append('cv_file', cv_file);

    try{
        return  await axios.post('/cv_processor', formData,
            {
                baseURL,
                onUploadProgress: progressEvent => {
                    let percentCompleted = Math.floor(progressEvent.loaded / progressEvent.total * 100)
                    console.log('completed: ', percentCompleted)
                    onProgress(percentCompleted)
                },
                headers: {
                    'Content-Type': 'application/json',
                }
            });

    }catch (e) {
        throw e
    }
}
