import {Container, Navbar} from "react-bootstrap";

export default ()=>{
    return (
        <Navbar>
            <Container>
                <Navbar.Brand href="#home">Job Finder</Navbar.Brand>
                <Navbar.Toggle />
                <Navbar.Collapse className="justify-content-end">
                    <Navbar.Text>
                        The Job to Match Your Skills is Just Minutes Away
                    </Navbar.Text>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}