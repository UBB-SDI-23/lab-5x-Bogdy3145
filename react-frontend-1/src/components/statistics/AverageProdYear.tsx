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
import ArrowUpwardIcon from "@mui/icons-material/ArrowUpward";
import ArrowDownwardIcon from "@mui/icons-material/ArrowDownward";
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
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc'); // initial sort order is ascending

  useEffect(() => {
    setLoading(true);
    axios
      .get(`${GlobalURL}/statistic/`)
      .then((response) => {
        setStatistics(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setLoading(false);
      });
  }, []);

  const handleSortOrderChange = () => {
    setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc'); // toggle sort order between ascending and descending
  };

  const sortedStatistics = statistics.sort((a, b) => {
    if (sortOrder === 'asc') {
      return a.avg_production_year - b.avg_production_year;
    } else {
      return b.avg_production_year - a.avg_production_year;
    }
  });

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
                <TableCell>CarBrand</TableCell>
                <TableCell align="right">
                  <Tooltip title="Sort by Average Production Year" arrow>
                    <IconButton onClick={handleSortOrderChange}>
                      {sortOrder === 'asc' ? <ArrowUpwardIcon /> : <ArrowDownwardIcon />}
                    </IconButton>
                  </Tooltip>
                  Avg_Production_Year
                </TableCell>
                <TableCell align="right">Car_Count</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {sortedStatistics.map((statistic, index) => (
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