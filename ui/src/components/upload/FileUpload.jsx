import React, {useCallback, useEffect, useState} from "react"
import {useDropzone} from "react-dropzone"
import FileUploadWithProgress from "./FileUploadWithProgress";
import {Grid} from "@material-ui/core";
import {useField} from "formik";
import {Alert} from "@mui/material";

export default ({name})=>{

    const [_,__, helpers] = useField(name)

    const [file, setFile] = useState({})
    const maxSize = 1048576

    const onDrop = useCallback(acceptedFiles => {
        setFile(acceptedFiles[0])
        console.log('All Files',acceptedFiles)
        console.log('Single File',acceptedFiles[0])
        console.log('File Name', acceptedFiles[0].name)
    }, [])

    useEffect(()=> {
        helpers.setValue(file)
        helpers.setTouched(true)
    },[file])

    const {getRootProps, getInputProps, isDragActive, isDragReject, acceptedFiles, fileRejections} = useDropzone({
        onDrop,
        maxFiles: 1,
        accept: ['.doc', '.docx', 'application/pdf', 'application/msword'],
        minSize: 0,
        maxSize
    })
    const isFileTooLarge = fileRejections.length > 0 && fileRejections[0].size > maxSize;

    return (
        <>
            <Grid style={{height: '200px'}} item {...getRootProps()}>
                <input {...getInputProps()} />
                {
                    !isDragActive &&
                    <p align="center" style={{marginTop: '50px'}}>Drag 'n' drop your resume here, or click to select it for job matching<br/>
                        <em>(Only *.pdf and *.docx images will be accepted)</em> </p>
                }
                {isDragActive && !isDragReject && <p align="center" style={{marginTop: '50px'}}>Drop the resume here ...</p>}
                {isDragReject && <p align="center">File type not accepted</p>}
                {isFileTooLarge && (
                    <div className="text-danger mt-2">
                        File is too large.
                    </div>
                )}
                {acceptedFiles.length > 0 && acceptedFiles.map(acceptedFile => (
                    <Alert severity="success">{acceptedFile.name}</Alert>
                ))}

                {acceptedFiles.length > 0 &&
                <FileUploadWithProgress file={file}/>
                }


                {/*{JSON.stringify(acceptedFiles)}*/}
            </Grid>

        </>

    )
}