WITH root_requests AS (
  SELECT *
  FROM requests
  WHERE host = 'balancer.test.yandex.ru' AND parent_request_id IS NULL
),
sub_requests AS (
  SELECT *
  FROM requests
  WHERE host != 'balancer.test.yandex.ru'
)
SELECT AVG(network_time_ms) AS avg_network_time_ms
FROM (
  SELECT root_request.request_id,
         SUM(
           EXTRACT(EPOCH FROM (response_received.datetime - request_sent.datetime)) * 1000
           - COALESCE(
               SUBQUERY1.sub_time_ms,
               0
             )
           - COALESCE(
               SUBQUERY2.sub_time_ms,
               0
             )
         ) AS network_time_ms
  FROM root_requests AS root_request
  LEFT JOIN (
    SELECT
      request_id,
      SUM(
        EXTRACT(EPOCH FROM (response_received.datetime - request_sent.datetime)) * 1000
      ) AS sub_time_ms
    FROM sub_requests
    WHERE type IN ('RequestSent', 'ResponseReceived')
    GROUP BY request_id
  ) AS SUBQUERY1
  ON root_request.request_id = SUBQUERY1.request_id
  LEFT JOIN (
    SELECT
      parent_request_id,
      SUM(
        EXTRACT(EPOCH FROM (response_received.datetime - request_sent.datetime)) * 1000
      ) AS sub_time_ms
    FROM sub_requests
    WHERE type IN ('RequestReceived', 'ResponseSent')
    GROUP BY parent_request_id
  ) AS SUBQUERY2
  ON root_request.request_id = SUBQUERY2.parent_request_id
  LEFT JOIN sub_requests AS request_sent
  ON root_request.request_id = request_sent.parent_request_id AND request_sent.type = 'RequestSent'
  LEFT JOIN sub_requests AS response_received
  ON root_request.request_id = response_received.parent_request_id AND response_received.type = 'ResponseReceived'
  GROUP BY root_request.request_id
) AS network_time
