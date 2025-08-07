import { ChatInterface } from '@/components/chat/ChatInterface';

const Index = () => {
  const apiEndpoint = import.meta.env.VITE_API_ENDPOINT || 'YOUR_BACKEND_ENDPOINT_HERE';
  
  return (
    <div className="h-screen">
      <ChatInterface apiEndpoint={apiEndpoint} />
    </div>
  );
};

export default Index;
