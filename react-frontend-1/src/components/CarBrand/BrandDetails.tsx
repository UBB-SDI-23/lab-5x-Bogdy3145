import { Card, CardActions, CardContent, IconButton } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { CarBrand } from "../../models/CarBrand";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { GlobalURL } from "../../constants";
import { styled } from '@mui/material/styles';



export const BrandDetails = () => {
	const { brandId } = useParams();
	const [brand, setBrand] = useState<CarBrand>();

	useEffect(() => {
		const fetchBrand = async () => {
			
			const response = await fetch(`${GlobalURL}/brands/${brandId}`);
			const brand = await response.json();
			setBrand(brand);
		};
		fetchBrand();
	}, [brandId]);

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/brands`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<h1>Owner Details</h1>
					<p>LastName: {brand?.name}</p>
					
                    <p>FirstName: {brand?.founding_year}</p>
					
					<p>CNP: {brand?.owner_name}</p>
					
					<p>Email: {brand?.rarity}</p>

                    <p>Address: {brand?.hq_address}</p>
					
					<p>Cars:</p>
					<ol>
						{brand?.cars?.map((car) => (
							<li key={car.id}>
							{[ 
							  `${car.name} ${car.name}`,
							  <br key="1" />,
							  `Color: ${car.description}`,
							  <br key="2" />,
							  `Production Year: ${car.engine}`,
							  <br key="3" />,
							  `Seats: ${car.year}`,
							]}
						  </li>
							
						))}
					</ol>
				</CardContent>
				<CardActions>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/brands/${brandId}/edit`}>
						<EditIcon />
					</IconButton>

					<IconButton component={Link} sx={{ mr: 3 }} to={`/brands/${brandId}/delete`}>
						<DeleteForeverIcon sx={{ color: "red" }} />
					</IconButton>
				</CardActions>
			</Card>
		</Container>
	);
};