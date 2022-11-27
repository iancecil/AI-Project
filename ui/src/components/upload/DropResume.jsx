import React from "react"
import {Formik} from "formik"
import FileUpload from "./FileUpload";
import { Card, CardContent, Grid } from '@material-ui/core';

export default () =>{
    return (
        <Card>
            <CardContent>
                <Formik initialValues={{cv_file: {}}}
                >
                    {({values, errors, touched,
                          handleChange, handleBlur,
                          handleSubmit, isSubmitting,
                      }) => (

                        <form onSubmit={handleSubmit}>
                            <Grid container spacing={2} direction='column'>
                                <FileUpload name='cv_file'/>
                            </Grid>
                            {/*<button type="submit" disabled={isSubmitting}>*/}
                            {/*    Submit*/}
                            {/*</button>*/}
                            {/*{errors.password && touched.password && errors.password}*/}

                            {/*<pre>{JSON.stringify({ values, errors }, null, 4)}</pre>*/}
                        </form>
                    )}
                </Formik>
            </CardContent>
        </Card>
    )
}