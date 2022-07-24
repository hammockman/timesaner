# timesaner
A better UI for TimeSaver 3.0


## Background

"TimeSaver 3.0" (whose Help-About dialog box attributes "Vision Software") is a time tracking application in use by at least one medium sized company. The exe detailed properties includes no copyright information and claims the application was last modified 19/11/2001 4:09 PM.

The UI is painful and requires precision mouse input, something that is difficult on a laptop with a touchpad, even if you're not driving at the same time. It is also harder than necessary to fill larger chunks of a day with a single task.

![image](https://user-images.githubusercontent.com/6187172/180629940-c5906c68-f3a3-42fb-bab9-44e92c58818b.png)


## Roadmap

- [ ] Reverse engineer the file formats to allow a different tool to modify the local database
- [ ] Create a tool to modify the local timesheet.
- [ ] Reverse engineer the client-server protocol to allow a different tool to send timesheets to the company server.
- [ ] Create a complete replacement for the TimeSaver3.0 client.

### Feature List

* Currently a single click on a task code adds as a half-hour block to the currently selected day. It would be nice if double and triple clicks changed the duration to 4 h and 8h respectively.
* Automatically colour code (rather than the current manual colour selection).
* Random timesheet generation (maybe based on recent weeks).


## TimeSaver 3.0

"TimeSaver 3.0" (TS3) appears to like being installed at `c:\Timesaver`. Along with `TS2000.exe` and `tsico.ico` files the following files are present:

| filename | notes |
|--- |--- |
| `TS2000.DAT` | Saved on application exit. |
| `TS2000.ADM` | Saved on application exit.|
| `TS2000.tst` | The task list. Saved on application exit. |
| `TS2000.tau` | Empty file. Maybe used to store other user info for people with direct reports.|
| `TS_XXXXX.tsf` | `XXXXX` is a 5 digit employee code. This is the only file that is modified when the user saves the timesheer (Ctrl+s)|
| `TS_XXXXX.TMP` | Appears to be generated when a corresponding `.tsf` file cannot be saved. |

At startup TS3 retrieves task structure from a company server. 



### `.tsf` format

