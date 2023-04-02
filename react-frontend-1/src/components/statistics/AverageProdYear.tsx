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
import { Link } from "react-router-dom";
import { CarBrand } from "../../models/CarBrand";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import { GlobalURL } from "../../constants";
import { useState, useEffect } from "react";
import axios from "axios";

interface Statistic {
	id: number;
	name: string;
	avg_production_year: number;
	car_count: number;
  }
export const AverageProdYear = () => {
    const [statistics, setStatistics] = useState<Statistic[]>([]);
  const [loading, setLoading] = useState(false);
  useEffect(() => {
	setLoading(true);
	axios.get(`${GlobalURL}/statistic/`)
	  .then(response => {
        console.log(response.data);
		setStatistics(response.data);
		setLoading(false);
	  })
	  .catch(error => {
		console.error(error);
		setLoading(false);
	  });
  }, []);

  return (
	<Container>
		<h1>Average Production Year Carbrands</h1>
		<p>Here we have carbrands ordered by average production year of their existent cars</p>
		{loading && <CircularProgress />}
		{!loading && statistics.length === 0 && <p>No statistic found</p>}
		
		{!loading && statistics.length > 0 && (
			<TableContainer component={Paper}>
				<Table sx={{ minWidth: 650 }} aria-label="simple table">
					<TableHead>
						<TableRow>
							<TableCell>#</TableCell>
							<TableCell >CarBrand</TableCell>
							<TableCell align="right">Avg_Production_Year</TableCell>
							<TableCell align="right">Car_Count</TableCell>
						   
						
						</TableRow>
					</TableHead>
					<TableBody>
				{statistics.map((statistic, index) => (
					<TableRow key={statistic.id}>
						<TableCell>{index + 1}</TableCell>
						<TableCell>{statistic.name}</TableCell>
						<TableCell align="right">{statistic.avg_production_year}</TableCell>
						<TableCell align="right">{statistic.car_count}</TableCell>
					</TableRow>
				))}
			</TableBody>
						
				</Table>
			</TableContainer>
		)}
	</Container>
);
};

//export default AverageProdYear;