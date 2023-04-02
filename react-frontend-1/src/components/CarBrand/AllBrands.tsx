import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
} from "@mui/material";
import axios from "axios";
import { styled } from '@mui/material/styles';
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { CarBrand } from "../../models/CarBrand";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import { GlobalURL } from "../../constants";

const StyledTableRow = styled(TableRow)`
  &:hover {
    background-color: #ecebed;
  }
`;

export const AllBrands = () => {
	const [loading, setLoading] = useState(false);
	const [brand, setBrand] = useState<CarBrand[]>([]);
	

	useEffect(() => {
		setLoading(true);
		axios.get(`${GlobalURL}/brands/`)
		  .then(response => {
			console.log(response.data);
			console.log(typeof response.data);
			setBrand(response.data);
			setLoading(false);
		  })
		  .catch(error => {
			console.error(error);
			setLoading(false);
		  });
	  }, []);
	return (
		<Container>
			<h1>All brands</h1>

			{loading && <CircularProgress />}
			{!loading && brand.length === 0 && <p>No brands found</p>}
			{!loading && (
				<IconButton component={Link} sx={{ mr: 3 }} to={`/brands/add`}>
					<Tooltip title="Add a new brand" arrow>
						<AddIcon color="primary" />
					</Tooltip>
				</IconButton>
			)}
			{!loading && brand.length > 0 && (
				<TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell>#</TableCell>
								<TableCell align="right">Name</TableCell>
								<TableCell align="right">Year</TableCell>
								<TableCell align="right">Owner</TableCell>
                                <TableCell align="right">Rarity</TableCell>
                                <TableCell align="right">Hq_Address</TableCell>
                            
								<TableCell align="center">Operations</TableCell>
							</TableRow>
						</TableHead>
						<TableBody>
							{brand.map((brand, index) => (
								<TableRow key={brand.id}>
									<TableCell component="th" scope="row">
										{index + 1}
									</TableCell>
                                    <TableCell align="right">{brand.name}</TableCell>
                                    <TableCell align="right">{brand.founding_year}</TableCell>
									<TableCell component="th" scope="row">
										<Link to={`/brands/${brand.id}/details`} title="View brand details">
											{brand.owner_name}
										</Link>
									</TableCell>
									<TableCell align="right">{brand.rarity}</TableCell>
									<TableCell align="right">{brand.hq_address}</TableCell>
                                    
									<TableCell align="right">

										<IconButton
											component={Link}
											sx={{ mr: 3 }}
											to={`/brands/${brand.id}/details`}>
											<Tooltip title="View brand details" arrow>
												<ReadMoreIcon color="primary" />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/brands/${brand.id}/edit`}>
											<EditIcon />
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/brands/${brand.id}/delete`}>
											<DeleteForeverIcon sx={{ color: "red" }} />
										</IconButton>
									</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			)}
		</Container>
	);
};