import {
    Button,
    Card,
    CardActions,
    CardContent,
    CircularProgress,
    Container,
    IconButton,
    TextField,
  } from "@mui/material";
  import { useEffect, useState } from "react";
  import { Link, useNavigate, useParams } from "react-router-dom";
  import { CarBrand } from "../../models/CarBrand";
  import ArrowBackIcon from "@mui/icons-material/ArrowBack";
  import axios from "axios";
  import { GlobalURL } from "../../constants";
  
  export const BrandUpdate = () => {
    const navigate = useNavigate();
    const { brandId } = useParams();
  
    const [loading, setLoading] = useState(true);
    const [brand, setBrand] = useState<CarBrand | null>(null);
  
    useEffect(() => {
      const fetchBrand = async () => {
        try {
          const response = await axios.get<CarBrand>(
            `${GlobalURL}/brands/${brandId}`
          );
          setBrand(response.data);
        } catch (error) {
          console.log(error);
        } finally {
          setLoading(false);
        }
      };
      fetchBrand();
    }, [brandId]);
  
    const updateBrand = async (event: { preventDefault: () => void }) => {
      event.preventDefault();
      try {
        await axios.put(`${GlobalURL}/brands/${brandId}`, brand);
        navigate(`/brands/`);
      } catch (error) {
        console.log(error);
      }
    };
  
  
    return (
      <Container>
        {loading && <CircularProgress />}
  
        {!loading && !brand && <div>Brand not found</div>}
  
        {!loading && brand && (
          <Card>
            <CardContent>
              <IconButton
                component={Link}
                sx={{ mr: 3 }}
                to={`/brands/${brandId}`}
              >
                <ArrowBackIcon />
              </IconButton>{" "}
              <form onSubmit={updateBrand}>
                <TextField
                  value={brand.name}
                  id="name"
                  label="name"
                  variant="outlined"
                  fullWidth
                  sx={{ mb: 2 }}
                  onChange={(event) =>
                    setBrand({ ...brand, name: event.target.value })
                  }
                />
                <TextField
                  value={brand.founding_year}
                  id="founding_year"
                  label="founding_year"
                  variant="outlined"
                  fullWidth
                  sx={{ mb: 2 }}
                  onChange={(event) =>
                    setBrand({ ...brand, founding_year: event.target.value })
                  }
                />
  
                <TextField
                  value={brand.owner_name}
                  id="owner_name"
                  label="owner_name"
                  variant="outlined"
                  fullWidth
                  sx={{ mb: 2 }}
                  onChange={(event) =>
                    setBrand({ ...brand, owner_name: event.target.value })
                  }
                />
  
                <TextField
                  value={brand.rarity}
                  id="rarity"
                  label="rarity"
                  variant="outlined"
                  fullWidth
                  sx={{ mb: 2 }}
                  onChange={(event) =>
                    setBrand({ ...brand, rarity: event.target.value })
                  }
                />
                <TextField
                  value={brand.hq_address}
                  id="hq_address"
                  label="hq_address"
                  variant="outlined"
                  fullWidth
                  sx={{ mb: 2 }}
                  onChange={(event) =>
                    setBrand({ ...brand, hq_address: event.target.value })
                  }
                />
  
                <Button type="submit">Update Brand</Button>
              </form>
            </CardContent>
            <CardActions></CardActions>
          </Card>
        )}
      </Container>
    );
  };