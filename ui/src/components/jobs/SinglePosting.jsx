import {
    Avatar,
    Button, Card, CardActions, CardContent, CardHeader,
    Divider,
    Grid,
    Typography,
    colors
} from "@mui/material";


export default ({jobTitle, companyName, postDate, jobSummary, jobUrl}) =>{

    return (
        <Grid item >
            <Card sx={{ }} style={{marginBottom: '20px'}}>
                <CardHeader
                    avatar={
                        <Avatar sx={{ bgcolor: colors.red[500] }} aria-label="recipe">
                            {companyName.charAt(0)}
                        </Avatar>
                    }

                    title={companyName}
                    subheader={postDate.replace("Posted"," ")}
                />
                <CardContent>
                    <Typography gutterBottom variant="body1" component="div">
                        {jobTitle}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {jobSummary}
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button href={jobUrl} target='_blank' size="small">View Job</Button>
                </CardActions>
            </Card>
            <Divider variant="inset" component="li" />
        </Grid>
    )
}