


func CallMeWithDeadLine(url string, output interface{}) (int) {

	// Setup a deadline of 5ms
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Millisecond)
    defer cancel()

    // Make a new requets object
    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        return -1
    }

	// Build a request with timeout
    resp, err := http.DefaultClient.Do(req.WithContext(ctx))
    defer func() {
        if resp != nil && resp.Body != nil {
            resp.Body.Close()
        }
    }()

    if err != nil {
        return 500
    }

    body, _ := ioutil.ReadAll(resp.Body)
    if err := json.Unmarshal(body, output); err != nil {
        panic(err)
    }

    return resp.StatusCode
}

