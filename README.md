# Pi User History Viewer

A simple, interactive front-end application to view, filter, edit, and analyze Raspberry Pi user history data.

## Features

### 📊 View Data
- Clean, responsive table view of all user history records
- Real-time statistics dashboard showing:
  - Total records
  - Successful actions
  - Failed actions
  - Unique users

### 🔍 Filter & Search
- **Search**: Real-time search across username, action, device, and IP address
- **Filter by Status**: View only successful or failed actions
- **Filter by Action**: Filter by specific action types (login, logout, file_upload, etc.)
- **Filter by Device**: Filter by Raspberry Pi device model
- **Sort**: Click any column header to sort ascending/descending

### ✏️ Edit Data
- **Edit Records**: Click "Edit" button to modify any record
- **Add New Records**: Click "+ Add New" to create new entries
- **Delete Records**: Remove unwanted records with confirmation
- **Form Validation**: Ensures data integrity with required fields and IP address validation

### 💾 Export
- Export current data to JSON file
- Download modified data for backup or sharing

## Usage

### Getting Started

1. **Open the Application**
   - Simply open `index.html` in any modern web browser
   - The application works entirely client-side, no server required

2. **View Your Data**
   - The application loads data from `copy-of-pi-user-history.json`
   - All records are displayed in an interactive table

3. **Search and Filter**
   - Use the search box to find specific records
   - Apply filters using the dropdown menus
   - Click "Reset Filters" to clear all filters

4. **Edit Records**
   - Click "Edit" on any row to modify that record
   - Click "+ Add New" to create a new record
   - Fill in the form and click "Save Changes"

5. **Delete Records**
   - Click "Delete" on any row
   - Confirm the deletion when prompted

6. **Export Data**
   - Click "Export JSON" to download the current dataset
   - The file will be saved as `pi-user-history-export.json`

## Data Structure

The application expects JSON data in the following format:

```json
[
  {
    "id": 1,
    "username": "alice_pi",
    "timestamp": "2025-01-15T10:30:00Z",
    "action": "login",
    "device": "Raspberry Pi 4",
    "ip_address": "192.168.1.100",
    "duration_minutes": 45,
    "status": "success"
  }
]
```

### Fields:
- **id**: Unique identifier (number)
- **username**: Username of the user (string)
- **timestamp**: ISO 8601 formatted timestamp (string)
- **action**: Action performed (string)
- **device**: Raspberry Pi device model (string)
- **ip_address**: IPv4 address (string)
- **duration_minutes**: Duration of action in minutes (number)
- **status**: "success" or "failed" (string)

## Customization

### Adding Your Own Data

Replace the contents of `copy-of-pi-user-history.json` with your own user history data following the same structure.

### Styling

The application uses inline CSS for easy customization. Edit the `<style>` section in `index.html` to change:
- Colors and theme
- Layout and spacing
- Font sizes and families
- Responsive breakpoints

## Browser Compatibility

Works with all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## Files

- `index.html` - Main application file
- `copy-of-pi-user-history.json` - Sample data file
- `README.md` - This documentation

## Notes

- All changes are stored in browser memory only
- Use the "Export JSON" feature to save your changes permanently
- The application requires JavaScript to be enabled
- Data is loaded from a local JSON file, so it must be in the same directory as index.html
Misc data
