import { Button, Card, CardActions, CardContent, IconButton, TextField } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

import { CarBrand } from "../../models/CarBrand";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { GlobalURL } from "../../constants";

export const BrandAdd = () => {
	const navigate = useNavigate();

	const [brand, setBrand] = useState<CarBrand>({
		name:"",
        founding_year: "",
        owner_name:"",
        rarity:"",
        hq_address:"",
	});

	const addBrand = async (event: { preventDefault: () => void }) => {
		event.preventDefault();
		try {
			await axios.post(`${GlobalURL}/brands/`, brand);
			navigate("/brands");
		} catch (error) {
			console.log(error);
		}
	};

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/brands`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<form onSubmit={addBrand}>
						<TextField
							id="name"
							label="name"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>)=> setBrand({ ...brand, name: event.target.value })}
						/>
                        <TextField
							id="founding_year"
							label="founding_year"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>) => setBrand({ ...brand, founding_year: event.target.value })}
						/>
						<TextField
							id="owner_name"
							label="owner_name"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>) => setBrand({ ...brand, owner_name: event.target.value })}
						/>
						 <TextField
							id="rarity"
							label="rarity"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>) => setBrand({ ...brand, rarity: event.target.value })}
						/>
						 <TextField
							id="hq_address"
							label="hq_address"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event: React.ChangeEvent<HTMLInputElement>) => setBrand({ ...brand, hq_address: event.target.value })}
						/>

						<Button type="submit">Add Brand</Button>
					</form>
				</CardContent>
				<CardActions></CardActions>
			</Card>
		</Container>
	);
};
