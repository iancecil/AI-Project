import {useEffect, useState, useReducer, useContext} from "react";
import {Grid, LinearProgress} from "@material-ui/core";
import { postResume} from "../../services/resumeService";
import {Context} from "../../state/store";


export default ({file})=>{

    const [state, dispatch] = useContext(Context)

    const [progress, setProgress] = useState(0)

    useEffect(()=>{

        const upload = async ()=>{
            try{
                dispatch({type: 'GET_JOBS'})
                const resp = await postResume(file, setProgress);

                console.log('RESPONSE', resp.data.data)
                dispatch({type: 'GET_JOBS_RES', payload: resp.data.data})

            }catch (err){
                if (err.response){
                    console.log('ERROR Retrieving ....', err.response)
                }else {
                    console.log('ERROR', err)
                }
                // dispatch({type: 'GET_JOBS_ERR', payload: 'Unable to upload file'})
            }
        }
        upload()

    },[file])


    return (
        <Grid item>
            <LinearProgress variant="determinate" value={progress}/>
            {console.log(JSON.stringify(state))}
        </Grid>
    )
}
