import { Container, Card, CardContent, IconButton, CardActions, Button } from "@mui/material";
import { Link, useNavigate, useParams } from "react-router-dom";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { GlobalURL } from "../../constants";

export const BrandDelete = () => {
	const { brandId } = useParams();
	const navigate = useNavigate();

	const handleDelete = async (event: { preventDefault: () => void }) => {
		event.preventDefault();
		await axios.delete(`${GlobalURL}/brands/${brandId}`);
		
		navigate("/brands");
	};

	const handleCancel = (event: { preventDefault: () => void }) => {
		event.preventDefault();
		
		navigate("/brands");
	};

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/brands`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					Are you sure you want to delete this Brand? This cannot be undone!
				</CardContent>
				<CardActions>
					<Button onClick={handleDelete}>Delete it</Button>
					<Button onClick={handleCancel}>Cancel</Button>
				</CardActions>
			</Card>
		</Container>
	);
};
