import {useEffect, useState, useContext} from 'react'
import {Grid, List, Typography} from "@mui/material";
import SinglePosting from "./SinglePosting";
import jobResults from '../../data/jobResults2.json'
import CircularIndeterminate from "../Spinner";
import {Context} from "../../state/store";

export default () =>{

    const [state, dispatch] = useContext(Context)
    // const [loading, setLoading] = useState(false)
    // const [jobData, setJobData] = useState([])

    useEffect(()=>{
        // setTimeout(()=>{
        //     setLoading(true)
        // },15000)
        // // dispatch({type: 'GET_JOBS_RES', payload: jobResults.data})
        //
        // setTimeout(()=>{
        //     setLoading(false)
        //     setJobData(jobResults.data)
        // }, 240000) //240000 - 4 minutes
        console.log('State from job postings',state)

    },[state])
   const renderJobs = ()=>{
       return state.jobs.map(job=>{
           return (
               <div key={state.jobs.JobID}>
                   <SinglePosting
                       companyName={job.Company}
                       jobSummary={job.Summary}
                       postDate={job.PostDate}
                       jobUrl={job.JobURL}
                       jobTitle={job.JobTitle}
                   />
               </div>
           )
       })
   }

   if (state.loading) return (
       <Grid item p={10} pl={60}>
           <CircularIndeterminate/>
       </Grid>

   )
   if (!state.loading && state.jobs.length <= 0) return <p style={{marginTop: '50px'}}align="center">No data yet</p>

    return (
        <Grid item>
            <Typography mt={2} variant="h5" gutterBottom component="div">
                Top Job Results: ({state.jobs[0].JobType})
            </Typography>
            <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
                {renderJobs()}
            </List>
        </Grid>

    )
}