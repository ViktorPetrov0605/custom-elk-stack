# AliExpress Search URL Parameters

## Base URL Structure

```
https://www.aliexpress.com/wholesale?SearchText=KEYWORD&PARAMETERS
```

Redirects to:
```
https://www.aliexpress.com/w/wholesale-KEYWORD.html?PARAMETERS
```

**Note**: Parameters are case-insensitive but get lowercased in the redirect.

---

## Confirmed Working Parameters

| Parameter | Values | Description |
|-----------|--------|-------------|
| `SearchText` | URL-encoded string | Main search query (required) |
| `minPrice` | Number (e.g., 50) | Minimum price filter |
| `maxPrice` | Number (e.g., 200) | Maximum price filter |
| `sortType` | `price_asc`, `price_desc`, `orders`, `newest` | Sort order |
| `isFreeShip` | `y` | Free shipping only |
| `shipFromCountry` | 2-letter code (CN, US, etc.) | Country shipping from |
| `shipToCountry` | 2-letter code (BG, US, etc.) | Country shipping to |
| `page` | Number | Pagination (1, 2, 3...) |
| `SearchType` | `product` | Filter to products only |

---

## Parameter Details

### Price Range
```
minPrice=100&maxPrice=500
```

### Sort Order
| Value | Description |
|-------|-------------|
| `sortType=price_asc` | Price: Low to High |
| `sortType=price_desc` | Price: High to Low |
| `sortType=orders` | Best Selling |
| `sortType=newest` | Newest Arrivals |

### Shipping
```
isFreeShip=y                    # Free shipping only
shipFromCountry=CN             # Ship from China
shipFromCountry=US             # Ship from US
shipToCountry=BG               # Ship to Bulgaria
```

### Pagination
```
page=1   # First page
page=2   # Second page
```

---

## Example URLs

### Basic Search
```
https://www.aliexpress.com/wholesale?SearchText=10TB+hard+disk
```

### With Price Filter (100-500 USD)
```
https://www.aliexpress.com/wholesale?SearchText=ssd&minPrice=100&maxPrice=500
```

### Cheapest + Free Shipping
```
https://www.aliexpress.com/wholesale?SearchText=headphones&sortType=price_asc&isFreeShip=y
```

### Ship from China to Bulgaria
```
https://www.aliexpress.com/wholesale?SearchText=laptop&shipFromCountry=CN&shipToCountry=BG&minPrice=300&maxPrice=800
```

### Full Combo
```
https://www.aliexpress.com/wholesale?SearchText=external+hard+drive+10tb&minPrice=50&maxPrice=300&sortType=price_asc&isFreeShip=y&shipFromCountry=CN&page=1
```

---

## Data Extraction Notes

- AliExpress pages load product data **dynamically** via JavaScript
- Simple `curl` or `fetch` returns skeleton HTML without products
- **To get actual data**, use:
  - Browser automation (undetected-chromedriver)
  - Headless browser with JavaScript execution
  - Wait for network requests to complete
  - Or find internal API endpoints (more complex)

---

## Quick Test Commands

### Verify URL Redirects
```bash
curl -s -I "https://www.aliexpress.com/wholesale?SearchText=laptop&minPrice=500&maxPrice=1000&sortType=price_asc" | grep location
```

Expected: Shows redirect URL with preserved parameters

### Check Parameter Preservation
Parameters are lowercased but preserved:
- `minPrice=500` → `minprice=500`
- `sortType=price_asc` → `sorttype=price_asc`

---

## Limitations

1. **Bot Protection**: Heavy scraping triggers CAPTCHA/blocks
2. **Dynamic Content**: Products load via JS, not in initial HTML
3. **Rate Limiting**: Frequent requests will be blocked
4. **Authentication**: Some features require login cookies

---

## Alternatives for Data Extraction

| Method | Pros | Cons |
|--------|------|------|
| URL + Browser Automation | Full data, reliable | Slower, resource-heavy |
| AliExpress Open API | Structured data | Requires API key, limited access |
| Third-party APIs (RapidAPI) | Easy integration | Paid, rate limits |
| RSS Feeds | Simple | Limited data |

---

*Document generated from empirical testing and community documentation*
