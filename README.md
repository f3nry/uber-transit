### OVERVIEW

Didn't want to use Uber? Fine. Here you go.

### Architecture

This app ingests the 511.org real-time departure API and provides information
about departures at the nearest transit stops.

The app is backed by Postgres with the following schema:

agencies:
  - id: integer
  - name: string
  - has_direction: boolean
  - mode: string

routes:
  - id: integer
  - agency_id: integer
  - name: string
  - code: integer

stops:
  - route_id: integer
  - name: string
  - stop_code: integer
