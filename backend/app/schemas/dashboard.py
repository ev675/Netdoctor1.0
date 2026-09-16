from pydantic import BaseModel, Field


class Metric(BaseModel):
    value: float
    unit: str
    status: str
    min_value: float | None = None
    max_value: float | None = None


class HealthScore(BaseModel):
    score: int = Field(ge=0, le=100)
    status: str
    message: str


class NetworkInfo(BaseModel):
    name: str
    connection_type: str
    status: str
    ip_address: str | None = None
    isp: str | None = None


class DiagnosisLayer(BaseModel):
    name: str
    status: str
    message: str


class DiagnosisSummary(BaseModel):
    title: str
    severity: str
    likely_problem_area: str
    confidence: int = Field(ge=0, le=100)
    evidence: list[str]


class TracerouteHop(BaseModel):
    hop: int
    ip_address: str
    hostname: str | None = None
    latency_ms: float | None = None
    packet_loss_percent: float = 0


class DnsServerResult(BaseModel):
    server: str
    latency_ms: float
    status: str


class DestinationResult(BaseModel):
    destination: str
    latency_ms: float
    status: str


class DashboardOverview(BaseModel):
    health_score: HealthScore

    latency: Metric
    jitter: Metric
    packet_loss: Metric
    dns_latency: Metric

    download_mbps: float
    upload_mbps: float

    network: NetworkInfo

    diagnosis_layers: list[DiagnosisLayer]
    diagnosis_summary: DiagnosisSummary

    traceroute: list[TracerouteHop]
    dns_benchmark: list[DnsServerResult]
    top_destinations: list[DestinationResult]