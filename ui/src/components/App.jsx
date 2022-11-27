import React, {useState} from "react"
import DropResume from "./upload/DropResume";
import JobPostings from "./jobs/JobPostings";
import {Container} from "@mui/material";
import 'bootstrap/dist/css/bootstrap.min.css';

import Navbar from "./Navbar";
import Store from "../state/store";


const App = ()=> {

    return (
        <Store>
            <Container>
                <Navbar/>
                <DropResume/>
                <JobPostings/>
            </Container>
        </Store>

    )
}

export default App